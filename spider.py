import argparse
import os
import requests

def main():
        parser = argparse.ArgumentParser(
                prog="spider",
                description="spider is a web scarper programme",
                epilog="thank you for using my programme"
        )
        parser.add_argument('-r' help="add recursive scan of the target")