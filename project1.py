import random
our_tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lucky_tickets = [2, 6, 9]
lucky_customers = []


def get_ticket_from_list(tickets):
    if not tickets:
        print("Sorry, we do not have a ticket")

    else:
        chooseTicket = random.choice(tickets)   # احفظ القيمة العشوائية للتذكرة
        print(f"Random Ticket : {chooseTicket}")
        tickets.remove(chooseTicket)            # من هنا احذف العنصر من القائمة
        return chooseTicket


def give_ticket_to_customer(ticket, name):      #  كيف هنا راح احدد مكان العنصر المدخل
    print(f"Congralutaion {name.upper()} \t you have get a new ticket. your ticket number: {ticket}")

def is_lucky_ticket(ticket, lucky_tickets):
    if ticket in lucky_tickets:
        return True

def add_customer_to_list(name, lucky_customers):

            lucky_customers.append(name) # اقوم باضافه اسم الزبون المحظوظ لقائمة العملاء


def main():
    while True:

        name = input("Want a ticket? Write your name \-->") # enter the name

        print(f"Hello\t{name}") # check stored name

        ticket = get_ticket_from_list(our_tickets) # call func

        # print(ticket) # check ticket list

        give_ticket_to_customer(ticket, name)
        # print(give_ticket_to_customer(ticket,name))


        if is_lucky_ticket(ticket, lucky_tickets):
            add_customer_to_list(name, lucky_customers)

        print(f'Lucky customers: {lucky_customers}')



if __name__ == '__main__':
    main()
