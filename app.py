import argparse
import json
import os
from datetime import date 

parser = argparse.ArgumentParser(description='a simple program to track expenses')

# Features of the program
parser.add_argument('command', choices=['add', 'update', 'delete', 'list', 'summary'])
parser.add_argument('-d', '--description', type=str)
parser.add_argument('-a', '--amount', type=float, nargs='?')
parser.add_argument('-i', '--id', type=int)
parser.add_argument('-m', '--month', type=int)

args = parser.parse_args()

filename = 'expenses.json'

# Check if JSON file exists
if os.path.exists(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        expenses = json.load(file)
else:
    expenses = []

# Add expenses
if args.command == 'add':
    
    if args.description is None or args.amount is None:
        parser.error('add requires description and amount')
    elif args.amount <= 0:
        parser.error('amount must be positive amount')
    else:
        new_expense = {
            'ID': max((expense['ID'] for expense in expenses), default=0) + 1,
            'Date': date.today().isoformat(),
            'Description': args.description,
            'Amount': args.amount
        }

        expenses.append(new_expense)
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(expenses, file, indent=4)
        print(f'Expense added successfully (ID: {new_expense["ID"]})')

# Update expenses
elif args.command == 'update':

    if args.id is None or args.description is None or args.amount is None:
        parser.error('update requires id, description, amount')
    elif args.id <= 0:
        parser.error('id must be a positive integer')
    elif args.amount <= 0:
        parser.error('amount must be positive amount')
    else:
        found = False
        for expense in expenses:
            if expense['ID'] == args.id:
                expense['Description'] = args.description
                expense['Amount'] = args.amount
                found = True
                break
        if not found:
            parser.error(f'Expense with ID: {args.id} is not found')
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(expenses, file, indent=4)
        print(f'Expense updated successfully (ID: {args.id})')

# Delete expenses
elif args.command == 'delete':

    if args.id is None:
        parser.error('delete requires id')
    elif args.id <= 0:
        parser.error('id must be a positive integer')
    else:
        found = False
        for expense in expenses:
            if expense['ID'] == args.id:
                expenses.remove(expense)
                found = True
                break
        if not found:
            parser.error(f'Expense with ID: {args.id} is not found')   
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(expenses, file, indent=4)
        print('Expense deleted successfully')

# List expenses
elif args.command == 'list':
    
    if not expenses:
        print('No expenses found')
    else:
        for expense in expenses:
            print(f'ID: {expense["ID"]}  Date: {expense["Date"]}  Description: {expense["Description"]}  Amount: {expense["Amount"]}')

# Summary of expenses
elif args.command == 'summary':
    
    if args.month is None:
        total_amount = 0
        for expense in expenses:
            total_amount += expense['Amount']
        print(f'Total expenses: ${total_amount}')
    elif args.month <= 0:
        parser.error('month must be a positive integer')
    else:
        total_amount = 0
        for expense in expenses:
            expense_date = date.fromisoformat(expense['Date'])
            if expense_date.month == args.month and expense_date.year == date.today().year:
                total_amount += expense['Amount']
        month_name = date(2026, args.month, 1).strftime('%B')
        print(f'Total expenses for {month_name}: ${total_amount}')