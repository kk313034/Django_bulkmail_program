from django.shortcuts import render,redirect
from django.core.mail import send_mail
from bulkmail.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from datetime import datetime
import csv
# Create your views here.

def test_mail(request):
    message = render_to_string('index.html', {'recipient_name': 'John Doe'})
    print(message)
    # with open('C:/Users/user/Desktop/mailtest.csv', 'r') as file:
    with open('D:/AIM/mail/mailtest.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        # message = render_to_string('index.html', {'recipient_name': 'John Doe'})
        report = []
        for row in reader:
            recipient_email = row
            curr_datetime=datetime.now()
            print(recipient_email,curr_datetime,"kkkkkkkkk")
                        # send_mail("User data: ",f"Test mail sent successfully",EMAIL_HOST_USER,[recipient_email])
            send_mail("User data: ",'',EMAIL_HOST_USER,[recipient_email],html_message=message,fail_silently=False)
            report.append({'recipient_email': recipient_email, 'sent_time': curr_datetime})

            # with open('C:/Users/user/Desktop/mailtest.txt', 'w') as file:
            #     # writer = csv.writer(file)
            #     # writer.writerows(curr_datetime)
            #     file.write(f'Sent to: {recipient_email}, Time: {curr_datetime}\n')
            with open('D:/AIM/mail/report.csv', mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['recipient_email', 'sent_time'])
                # writer.writeheader()
                writer.writerows(report)


        print("successfully")
        return render(request,'index.html')
def test(request):
    return render(request,"index.html")
