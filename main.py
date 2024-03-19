from time import sleep
from track.track import TrackESPFormatted
from track.trackRequest import TrackRequest, Player
from utils.serverSender import ServerData, load_server, update_server_data, read_server_data
from utils.cli import cli_parser
# import traceback
import datetime
import sys


def update_config(args) -> None:
    data = ServerData(args.ip, args.port)
    update_server_data(data)


def print_server_data(args) -> None:
    if not args.is_print_server:
        return

    data = read_server_data()
    print(f"Server:\n{data}")


def print_track_info(track) -> None:
    date = datetime.datetime.now()
    format_time = date.strftime("%H:%M:%S")
    print(f"[{format_time}]: {track};")


def send_track_to_server(track, server) -> None:
    esp_track = TrackESPFormatted(track)
    esp_track_json = esp_track.get_formatted_track_json()
    server.send(esp_track_json)


def main():
    try:
        args = cli_parser()
    except Exception as e:
        print(e)
        return

    update_config(args)
    print_server_data(args)

    track_request = TrackRequest(Player())
    server = load_server()

    while args.is_start:
        try:
            is_new_track = track_request.update()
            if not is_new_track:
                continue

            track = track_request.track
            send_track_to_server(track, server)

            if args.is_verbose:
                print_track_info(track)

            sleep(args.update_sec)
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as e:
            pass
            # print(traceback.format_exc())


if __name__ == '__main__':
    main()
