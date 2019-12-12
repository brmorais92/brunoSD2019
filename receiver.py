try:
        import pika

except Exception as e:
        print("Some modules are missings {}".format(e))

connection = pika.BlockingConnection(
        pika.ConnectionParameters(host =  'localhost'))
    
channel = connection.channel()
channel.queue_declare(queue = 'hello')

def callback (ch, method, properties, body):
        print("[x] Received %r" % body)

channel.basic_consume(
         queue = 'hello', on_message_callback = callback, auto_ack = True)


print(' [*] Waiting for masseges. To exit press CRTL+C')
 
channel.start_consuming()               
             

