import logging

class Note:
    gname = str()
    title = str()
    content = str()

    # generate txt and log files and writing if file already available
    def generate(self, gname, title, content):
        self.gname = gname
        self.title = title
        self.content = content

        # txt file writing part
        with open('input.txt', 'a+') as write_f:
            write_f.write(f'{self.gname}_{self.title}_{self.content}\n')
            
            # logging part

            logging.basicConfig(filename='data.txt', format='-------------------------\n%(asctime)s \n%(message)s', filemode='a+', level=logging.INFO)

            logging.info(
                f'E-Note Title: {self.title}\nE-Note Description: {self.content}\n\t\tNote Generator: {self.gname}'
            )

    # Viewing method for second menu choice
    def view(self):
        with open('input.txt', 'r') as read_f:
            for each_line in read_f:
                par_data = each_line.split('_')
                print('E-Note Generator Name:', par_data[0])
                print('E-Note Title:', par_data[1])
                print('E-Note Content:', par_data[2])
        
choice = 0

while True:
    # initializing instance of class
    b1 = Note()

    print('\n\t\tWelcome to python E-Note')
    print('\t\tPress 1 for generate Note ')
    print('\t\tPress 2 for view Note')
    print('\t\tpress 3 for exit\n')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        gname = input('Enter python E-Note Generator Name: ')

        while gname.isdigit():
            print('Error : Invalid Input')
            gname = input('Enter python E-Note Generator Name: ')

        title = input('Enter python E-Note Title: ')

        while title.isdigit():
            print('Error : Invalid Input')
            title = input('Enter python E-Note Title: ')

        content = input('Enter E-Note Content: ')

        b1.generate(gname, title, content)

    elif choice == 2:
        b1.view()

    elif choice == 3:
        break

    else:
        print('\t\tReenter the choice correctly!!!')
