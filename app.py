import math
from flask import Flask, render_template, request

app = Flask(__name__)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def insert_after(self, target, data):
        curr = self.head
        while curr:
            if str(curr.data) == str(target):
                node = Node(data)
                node.next = curr.next
                curr.next = node
                return True
            curr = curr.next
        return False

    def remove_at_beginning(self):
        if self.head:
            self.head = self.head.next

    def remove_at_end(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None

    def remove_target(self, target):
        if not self.head:
            return

        if str(self.head.data) == str(target):
            self.head = self.head.next
            return

        curr = self.head
        while curr.next:
            if str(curr.next.data) == str(target):
                curr.next = curr.next.next
                return
            curr = curr.next

    def to_list(self):
        items, curr = [], self.head
        while curr:
            items.append(curr.data)
            curr = curr.next
        return items


my_list = LinkedList()
my_list.insert_at_end("10")
my_list.insert_at_end("20")
my_list.insert_at_end("30")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        result = request.form.get('inputString', '').upper()
    return render_template('touppercase.html', result=result)


@app.route('/works/area/triangle', methods=['GET', 'POST'])
def atriangle():
    result = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', 0))
            height = float(request.form.get('height', 0))
            result = round(0.5 * base * height, 2)
        except ValueError:
            result = "Invalid input"
    return render_template('triangle.html', result=result)


@app.route('/works/area/circle', methods=['GET', 'POST'])
def acircle():
    result = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', 0))
            result = round(math.pi * radius * radius, 2)
        except ValueError:
            result = "Invalid input"
    return render_template('circle.html', result=result)


@app.route('/works/linkedlist', methods=['GET', 'POST'])
def linkedlist():
    if request.method == 'POST':
        action = request.form.get('action')
        val = request.form.get('value', '').strip()
        tgt = request.form.get('target', '').strip()

        if action == 'insert_beginning' and val:
            my_list.insert_at_beginning(val)
        elif action == 'insert_end' and val:
            my_list.insert_at_end(val)
        elif action == 'insert_after' and tgt and val:
            my_list.insert_after(tgt, val)
        elif action == 'remove_beginning':
            my_list.remove_at_beginning()
        elif action == 'remove_end':
            my_list.remove_at_end()
        elif action == 'remove_target' and tgt:
            my_list.remove_target(tgt)

    return render_template('linkedlist.html', items=my_list.to_list())


if __name__ == "__main__":
    app.run(debug=True)
