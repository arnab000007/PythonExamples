from Flipkart import Flipkart
from AnalyticsUpdate import AnalyticsUpdate
from EmailSender import EmailSender
from InvoiceGenerator import InvoiceGenerator

def main():

    # Generating Object so that indivisual Service
    # Can register itself

    ana = AnalyticsUpdate()
    ema = EmailSender()
    invoi = InvoiceGenerator()


    # Get the singleton instance
    flipkart: Flipkart = Flipkart.get_instance()

    # Calling Order Placement
    flipkart.orderPlaced()

    # Calling Order Cancelled
    flipkart.orderCancelled()

if __name__ == '__main__':
    main()