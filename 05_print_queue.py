from utils.input_data import InputData


class PrintQueue:
    def __init__(self):
        self.load_input()

    def load_input(self):
        self.input = InputData(5).input_data
        self.order_rules = self.clean_input("|")
        self.page_updates = self.clean_input(",")

    def clean_input(self, sep):
        raw = [i for i in self.input if sep in i]
        list_input = [i.split(sep) for i in raw if i != ""]
        list_input = [[int(j) for j in i] for i in list_input]
        return list_input

    def check_order(self, pages):
        correct_order = True
        for i in range(len(pages) - 1):
            if correct_order:
                page_set = {pages[i], pages[i + 1]}
                set_order = [
                    i for i in self.order_rules if i[0] in page_set and i[1] in page_set
                ]
                if set_order[0][0] != pages[i]:
                    correct_order = False
                    break
        return correct_order

    def get_correct_orders(self):
        self.checked_orders = [self.check_order(i) for i in self.page_updates]
        self.correct_orders = [
            pages for corr, pages in zip(self.checked_orders, self.page_updates) if corr
        ]
        self.incorrect_orders = [
            pages
            for corr, pages in zip(self.checked_orders, self.page_updates)
            if not corr
        ]
        print(f"There are {sum(self.checked_orders)} correct reprints")
        self.get_middle_numbers(self.correct_orders)

    def get_middle_numbers(self, orders):
        middle_numbers = [pages[int(len(pages) / 2)] for pages in orders]
        print(f"The sum of middle page numbers is {sum(middle_numbers)}")

    def fix_order(self, pages):
        for i in range(len(pages) - 1):
            first_page = pages[i]
            second_page = pages[i + 1]
            page_set = {first_page, second_page}
            set_order = [
                i for i in self.order_rules if i[0] in page_set and i[1] in page_set
            ]
            if set_order[0][0] != first_page:
                return self.fix_order(
                    pages[:i] + [pages[i + 1], pages[i]] + pages[i + 2 :]
                )

        return pages

    def correct_incorrect_orders(self):
        self.corrected_orders = [self.fix_order(i) for i in self.incorrect_orders]
        self.get_middle_numbers(self.corrected_orders)


if __name__ == "__main__":
    queue = PrintQueue()
    print("PART 1")
    queue.get_correct_orders()
    print("PART 2")
    queue.correct_incorrect_orders()
