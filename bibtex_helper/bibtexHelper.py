class bibtexHelper(object):
    def __init__(self, result):
        self.result = result

    def printInBibtexFormat(self, data):
        if data['entry_type_id'] == 1:
            self.printBook(data)
        elif data['entry_type_id'] == 2:
            self.printArticle(data)
        elif data['entry_type_id'] == 18:
            self.printMagazine(data)

    def printBook(self, data):
        authors = data['authors']
        title = data['title']
        year = data['publish_time']
        publisher = data['publisher']
        isbn = data['isbn']
        note = data['comments']
        address = data['publish_place']
        edition = data['numeration']
        series = data['series_name']
        pk = data['pk']
        text = f'@book{{{pk},\n  author =\t"{authors}", \
            \n  title =\t"{title}",\n  publisher =\t"{publisher}", \
            \n  year =\t{year},'
        if series != '' and series is not None:
            text += f'\n  series =\t"{series}",'
        if address != '' and address is not None:
            text += f'\n  address =\t"{address}",'
        if edition != '' and edition is not None:
            text += f'\n  edition =\t"{edition}",'
        if note != '' and note is not None:
            text += f'\n  note =\t"{note}",'
        if isbn != '' and isbn is not None:
            text += f'\n  isbn =\t"{isbn}",'
        print(text[0:len(text) - 1] + '\n}\n')

    def printArticle(self, data):
        item = data['item']
        authors = data['authors']
        title = data['title']
        year = data['publish_time']
        pk = data['pk']
        note = data['comments']
        issn = data['issn']
        pages = str(data['page_from'])+'-'+str(data['page_to'])
        journal = item['source_title']
        text = f'@article{{{pk},\n  author =\t"{authors}",\
                \n  title =\t"{title}",\n  journal =\t"{journal}",\
                \n  year =\t{year},'
        if pages != '' and pages is not None:
            text += f'\n  pages =\t{pages},'
        if note != '' and note is not None:
            text += f'\n  note =\t"{note}",'
        if issn != '' and issn is not None:
            text += f'\n  issn =\t"{issn}",'
        print(text[0:len(text) - 1] + '\n}\n')

    def printMagazine(self, data):
        authors = data['authors']
        title = data['title']
        year = data['publish_time']
        pk = data['pk']
        note = data['comments']
        number = data['numeration']
        address = data['publish_place']
        pages = data['number_of_pages']
        text = f'@misc{{{pk},'
        if authors != '' and authors is not None:
            text += f'\n  authors =\t"{authors}",'
        if title != '' and title is not None:
            text += f'\n  title =\t"{title}",'
        if year != '' and year is not None:
            text += f'\n  year =\t{year},'
        if address != '' and address is not None:
            text += f'\n  address =\t"{address}",'
        if note != '' and note is not None:
            text += f'\n  note =\t"{note}",'
        if number != '' and number is not None:
            text += f'\n  number =\t"{number}",'
        if pages != '' and pages is not None:
            text += f'\n  pages =\t.{pages},'
        print(text[0:len(text) - 1] + '\n}\n')
