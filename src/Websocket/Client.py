import websocket
import thread
import time
import constant as const
from datetime import datetime


def on_message(ws, message):
    print message


def on_error(ws, error):
    print error


def on_close(ws):
    print "### closed ###"
    # Attemp to reconnect with 2 seconds interval
    time.sleep(2)
    initiate()


def on_open(ws):
    print "### Initiating new websocket connection ###"

    def run(*args):
        for i in range(10):
            # Sending message with 1 second intervall
            time.sleep(5)
            date = datetime.now().replace(microsecond=0).isoformat(' ')
            # ws.send(json.dumps({'timestamp': date, 'data': i}))
        time.sleep(1)
        ws.close()
        print "thread terminating..."
    thread.start_new_thread(run, ())

def initiate():
    websocket.enableTrace(False)
    global ws
    ws = websocket.WebSocketApp(const.SERVER_URL,
        on_message = on_message,
        on_error = on_error,
        on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()

