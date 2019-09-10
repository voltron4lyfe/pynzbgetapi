
import sys
import argparse
from pynzbgetapi import NZBGetAPI


if __name__=="__main__":
        
    parser = argparse.ArgumentParser(description='Call NZBGet APIs.')
    parser.add_argument('host', help='the host')
    parser.add_argument('-u', '--username', dest='username', action='store', required=False,
                        help='the host')
    parser.add_argument('-pw', '--password', dest='password', action='store', required=False,
                        help='the host')                                                
    args = parser.parse_args()
    nzb_api = NZBGetAPI(args.host, port=6789, username=args.username, password=args.password, secure=False, verify_certificate=False)

    print(nzb_api.version())
    print(nzb_api.status())
    
    res = nzb_api.history()
    print(res)

    print(res.scan())
    print(res.status())

