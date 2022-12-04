import function
first_title_text = input("Write your first tagline: ")

first_paragraph = input("Write your description:")

second_title = 'House Makes'

second_paragraph= 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries,'

article = function.wp_title(first_title_text)+function.wp_paragraph(first_paragraph)+function.wp_title(second_title)+function.wp_paragraph(second_paragraph)
print(article)