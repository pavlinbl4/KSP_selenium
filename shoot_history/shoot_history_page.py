from autorization import autorization, end_selenium, check_shoot_id, open_page, work_to_history
from make_page_link import make_page_link
from _scrap_html import scrap_html
from multifile_fee_progect.save_page_html import save_html_page, read_html
from multifile_fee_progect.write_xlsx import write_rename_voc
from test_scripts.choose_input import chose_input

path_to_file = '/Volumes/big4photo/Documents/Kommersant/shoot_rename/shoot_story.xlsx'

shoot_id = chose_input()

autorization()

page_link = make_page_link(shoot_id)

open_page(page_link)

full_history_page_source = work_to_history()  # получаю данные со страницы истории

save_html_page(full_history_page_source)  # временно сохраняю страницу

file_renames = scrap_html(read_html())

write_rename_voc(path_to_file, file_renames, shoot_id)

end_selenium()
