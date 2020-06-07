from django.core.management.base import BaseCommand, CommandError
from review_management.models import Review
import collections

import os
from datetime import datetime

def read_file(file_path='/home/pawanvirsingh/Downloads/file_check.txt'):
    with open(file_path,encoding = "ISO-8859-1") as f:
        review_data = collections.OrderedDict()
        for line in f:
            if line !='\n':
                if ":" in  line:
                    key = line.split(":")[0].split("/")[1].strip(" ")
                    val = line.split(":")[1].strip(" ").strip("\n")
                    review_data[key] = val
                    if line.startswith("review/text"):
                       yield review_data
                       review_data = {}
                else:
                    #if line continue to next line
                    key = list(review_data.keys())[-1]
                    review_data[key] = review_data[key]+line.strip("\n")



class Command(BaseCommand):
    help = 'Loading the Review data in database '

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='?', type=str, default='data/foods.txt')
        parser.add_argument('chunk_size', nargs='?', type=int, default=1000, help="no of rows process in single chunk")

    def handle(self, *args, **options):
        file_path = options["file_path"]
        chunk_size = options["chunk_size"]
        # extension check
        file_var = file_path.split(".")
        if os.path.exists(file_path):
            if len(file_var) > 1:
                if file_var[-1] != "txt":
                    self.stdout.write(self.style.ERROR(f'Please choose Txt file '))
                    return
                else:
                    self.stdout.write(self.style.ERROR(f'Data Upload Started '))
            else:
                self.stdout.write(self.style.ERROR(f'Invalid file '))
                return
            #file reading
            count = 0
            row_number =0
            bulk_data_set = []
            for data_chunk in read_file(file_path):
                helpfulness_score = 0 if (int(data_chunk["helpfulness"].split("/")[1])==0) else \
                    int(data_chunk["helpfulness"].split("/")[0])/int(data_chunk["helpfulness"].split("/")[1])
                data = Review(
                        product_id=data_chunk["productId"],
                        user_id=data_chunk["userId"],
                        profile_name=data_chunk["profileName"],
                        helpfulness=data_chunk["helpfulness"],
                        score=data_chunk["score"],
                        time=data_chunk["time"],
                        summary=data_chunk["summary"],
                        text=data_chunk["text"],
                        helpfulness_score=helpfulness_score)
                bulk_data_set.append(data)
                count = count+1
                if count == chunk_size:
                    row_number +=count
                    Review.objects.bulk_create(bulk_data_set)
                    bulk_data_set = []
                    self.stdout.write(self.style.SUCCESS(f'successfully loaded  rows {row_number} '))
                    count = 0
            # if last chunk does not have 1000
            if bulk_data_set:
                Review.objects.bulk_create(bulk_data_set)
            self.stdout.write(self.style.SUCCESS(f'Upload successfully'))
        else:
            self.stdout.write(self.style.ERROR(f'file does not exists'))
