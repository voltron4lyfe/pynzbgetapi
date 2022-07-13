
import sys
import argparse
from pynzbgetapi import NZBGetAPI

if __name__=="__main__":

    # Define script arguments
    parser = argparse.ArgumentParser(description='Call NZBGet APIs.')
    parser.add_argument('host', help='the host', default='localhost')
    parser.add_argument('-p', '--port', dest='port', type=int, action='store', required=False, default='6789', help='Set the correct port')
    parser.add_argument('-u', '--username', dest='username', action='store', required=False, default="nzbget", help='a valid username')
    parser.add_argument('-pw', '--password', dest='password', action='store', required=False, default="tegbzn6789", help='a valid password')
    parser.add_argument('-s', '--secure', dest='secure', action='store', required=False, default=False, help='use True to set the connection to https, must specify the correct port to match')
    parser.add_argument('-v', '--verify-certificate', dest='verify_certificate', action='store', required=False, default="False", help='set True to enforce certificate validation')

    # Create connection
    args = parser.parse_args()
    nzb_api = NZBGetAPI(args.host, port=args.port, username=args.username, password=args.password, secure=args.secure, verify_certificate=args.verify_certificate)

    # Start Testing
    # Get Version
    print("\n\nGet Version")
    try:
        print(nzb_api.version())
    except:
        print("Error: Could not get version")
        sys.exit(1)

    # Get Status
    print("\n\nGet Status")
    try:
        print(nzb_api.status())
    except:
        print("Error: Could not get status")
        sys.exit(1)

    # Get Queue
    print("\n\nGet Queue")
    try:
        print(nzb_api.listgroups(number_of_log_entries='3'))
    except:
        print("Error: Could not get queue")
        sys.exit(1)

    # Limit Download & Reset
    print("\n\nLimit Download Rate")
    try:
        print(nzb_api.rate(5000))
    except:
        print("Error: Could not limit download speed, check user permissions")
        sys.exit(1)

    print("\n\nReset Download Rate")
    try:
        print(nzb_api.rate(0))
    except:
        print("Error: Could not reset download speed, check user permissions")
        sys.exit(1)

    # Pause & Resume Downloads
    print("\n\nPause Downloads")
    try:
        print(nzb_api.pausedownload())
    except:
        print("Error: Could not pause downloads, check user permissions")
        sys.exit(1)

    print("\n\nResume Downloads")
    try:
        print(nzb_api.resumedownload())
    except:
        print("Error: Could not resume downloads, check user permissions")
        sys.exit(1)

    # Get History
    res = nzb_api.history()

    print("\n\nGet History")
    try:
        print(res)
    except:
        print("Error: Could not get history")
        sys.exit(1)


    print("\n\nTesting Passed")
