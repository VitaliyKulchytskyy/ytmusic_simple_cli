import argparse
import re

TIME_DEFAULT = 20


def cli_parser():
    parser = argparse.ArgumentParser(prog='trackViewer',
                                     description='The YouTube Music track viewer.')
    parser.add_argument('-r', '--run',
                        dest='is_start',
                        action='store_true',
                        required=False,
                        help="run the client")
    parser.add_argument('-ip',
                        dest='ip',
                        action='store',
                        type=str,
                        required=False,
                        help="change or set the ip (IPv4) of the ESP32. Using: -ip \"127.0.0.1\"")
    parser.add_argument('-p', '--port',
                        dest='port',
                        action='store',
                        type=int,
                        required=False,
                        help="change or set the port. Using: -p 7777")
    parser.add_argument('-s', '--set',
                        dest='server_config',
                        action='store',
                        type=str,
                        default="",
                        required=False,
                        help="set the ip (IPv4) and the port simultaneously. Using: -s \"127.0.0.1:7777\"")
    parser.add_argument('-v', '--verbose',
                        dest='is_verbose',
                        action='store_true',
                        required=False,
                        help="print information about a received track")
    parser.add_argument('-u', '--update',
                        dest='update_sec',
                        action='store',
                        type=int,
                        default=TIME_DEFAULT,
                        required=False,
                        help=f"timer to requesting the player (in seconds). By default {TIME_DEFAULT} sec.")
    parser.add_argument('--server-data',
                        dest='is_print_server',
                        action='store_true',
                        required=False,
                        help=f"print the information about the server settings.")

    args = parser.parse_args()

    return validate_cli_args(args)


def is_port_correct(port: int) -> bool:
    return 0 <= port <= 99999


def is_ip_correct(ip: str) -> bool:
    output = re.match(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$", ip)
    return output is not None


def is_correct_update_timer(timer: int) -> bool:
    return 1 <= timer


def extract_ip_and_port(config) -> (str, int):
    pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*:\s*(\d{1,5})'
    match = re.match(pattern, config)

    if match:
        ip_address = match.group(1)
        port = int(match.group(2))
        return ip_address, port

    return None, None


def validate_cli_args(args):
    if args.port is not None and not is_port_correct(int(args.port)):
        raise Exception(
            f"[!] The port isn't correct (input={args.port}).\n"
            f"[?] 0 <= input_port <= 99999")

    if args.ip is not None and not is_ip_correct(args.ip):
        raise Exception(
            f"[!] The ip isn't correct (input={args.port}).\n"
            f"[?] The IPv4 format: [0-255].[0-255].[0-255].[0-255]")

    if args.is_verbose and not args.is_start:
        raise Exception(
            f"[!] You cannot see information about a received track if the program doesn't run.\n"
            f"[?] In a way to run the program use -r (or --run) flag.")

    if args.update_sec is not None and not is_correct_update_timer(args.update_sec):
        raise Exception(
            f"[!] You cannot set the update timer less than 1.\n"
            f"[?] Default value: {TIME_DEFAULT}. Recommended time range: 18-30 sec.")

    if args.server_config == '':
        return args

    extract_set = extract_ip_and_port(args.server_config)
    extract_ip = extract_set[0]
    extract_port = extract_set[1]

    if extract_ip is None or extract_port is None:
        raise Exception(f"[!] Incorrect server configuration (input={args.server_config}).\n"
                        f"[?] Example: \"127.0.0.1:7777\"")

    args.ip = extract_ip
    args.port = int(extract_port)

    return args
