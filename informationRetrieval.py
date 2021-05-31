import openpyxl
import re
loc = "test.xlsx"
# def extract_data():
#     for i in range(2, 5):
#         id = sheet.cell(i,1).value
#         name = sheet.cell(i,2).value
#         print(id, name)


#this method will prune the words and remove commas and dots and so on ...
#for example: سلام، --> سلام
def pruning_word(words):
    pruned_words = [x.replace('.', '').replace(':', '').replace('،', '').replace(';', '').replace('*', '')
                        .replace('**', '').replace('؛', '').replace(']', '').replace('[', '').replace('\"', '')
                        .replace('»', '').replace('?', '').replace('!', '').replace('#', '').replace('%', '')
                        .replace('^', '').replace('&', '').replace('(', '').replace(')', '').replace('؟', '')
                        .replace('۰', '').replace('۱', '').replace('۲', '').replace('۳', '').replace('۴', '')
                        .replace('۵', '').replace('۶', '').replace('۷', '').replace('۸', '').replace('۹', '') for x in words]

    term_to_remove = []
    for i in range(len(pruned_words)):
        if ('https' in pruned_words[i]) or (len(pruned_words[i]) >= 20) or (pruned_words[i].isdigit()) \
                or (pruned_words[i] == '+') or (len(pruned_words[i]) == 0):
            term_to_remove.append(pruned_words[i])
    for i in range(len(term_to_remove)):
        pruned_words.remove(term_to_remove[i])
    print(term_to_remove)
    return pruned_words


def tokenizer(text):
    words = pruning_word(text.split())
    words_without_duplicate = []
    [words_without_duplicate.append(word) for word in words if word not in words_without_duplicate]
    sorted_set = sorted(words_without_duplicate)
    return sorted_set


def excel_maker(sheet):
    row_num = sheet.max_row
    column_num = sheet.max_column
    print(row_num - 1, column_num)
    for i in range(2, row_num + 1):
        id = sheet.cell(i, 1).value
        text = sheet.cell(i, 2).value
        words = tokenizer(text)
        print(id, len(words))
        print(text)
        print(words)


def main():
    wb = openpyxl.load_workbook(loc)
    sheet = wb['Sheet1']
    # text = "با عرض سلام و خسته نباشید خدمت همه ی دوستان حاضر در جمع، این کد کسشر برای درس یازیابی اطلاعات است. این کد با خون در و کون پارهگی نوشته شده است."
    # text2 = "first fuck this is bullshit fuck this shit"
    excel_maker(sheet)


main()
