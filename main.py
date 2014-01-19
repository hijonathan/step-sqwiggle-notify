import sys
import sqwiggle

if len(sys.argv) < 4 :
    print('There should be 4 arguments')
    sys.exit(1)

token = str(sys.argv[1])
room_id = str(sys.argv[2])
message = str(sys.argv[3])

client = sqwiggle.Sqwiggle(token=token)
client.method('/messages', method='POST', parameters={'room_id': room_id, 'text': message, 'parse': False})
