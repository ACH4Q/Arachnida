import argparse
import os
import requests

def main():
        
        images = ['.jpg','.jpeg','.gif','.bmp','.png']
        parser = argparse.ArgumentParser(
                prog="spider",
                description="spider is a web scarper programme",
                epilog="thank you for using my programme"
        )
        parser.add_argument('-r', help="add recursive scan of the target")
        parser.add_argument('-l', help="indicates the maximum depth level of the recursive download")
        parser.add_argument('-p',default='./data/' , help="insert the path where the downloaded files will be stored")

        request = requests.request(
                data=""
        )