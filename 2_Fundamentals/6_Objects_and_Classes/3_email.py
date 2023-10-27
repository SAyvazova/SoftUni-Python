class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


list_of_emails = []
email_info = input()
while email_info != "Stop":
    sender, receiver, content = email_info.split()
    email = Email(sender, receiver, content)
    list_of_emails.append(email)
    email_info = input()

sent_indices = [int(index) for index in input().split(', ')]
for index in sent_indices:
    list_of_emails[index].send()

for current_email in list_of_emails:
    print(current_email.get_info())
