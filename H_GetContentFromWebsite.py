from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()

# Mở trang web
urls = [
    "https://tinhte.vn/thread/panasonic-bat-dau-san-xuat-pin-cong-nghe-moi-cho-xe-dien.3747964/",
    "https://tinhte.vn/thread/hinh-anh-xe-dien-xiaomi-dang-chay-tren-duong-dep-hon-ca-anh-dung.3747758/",
    "https://tinhte.vn/thread/new-mazda-cx-3-2024-ra-mat-tai-viet-nam-nang-cap-trang-bi-gia-tu-524-trieu-dong.3745833/",
    "https://tinhte.vn/thread/sau-2-nam-trien-khai-he-thong-tram-sac-xe-dien-vinfast-da-phat-trien-nhu-the-nao.3744752/",
    "https://tinhte.vn/thread/san-xuat-01-vien-pin-550-kg-xe-dien-tesla-can-gi.3747171/",
    "https://tinhte.vn/thread/infographic-tai-sao-xe-dien-la-xu-huong-cua-tuong-lai.3743397/",
    "https://tinhte.vn/thread/kia-sportage-hybrid-2024-ra-mat-moi-anh-em-tham.3747958/",
    "https://tinhte.vn/thread/mitsubishi-xforce-chot-lich-ra-mat-tai-viet-nam-vao-ngay-10-01-2024-voi-4-phien-ban-anh-em-da.3747668/",
    "https://tinhte.vn/thread/genesis-gv80-2025-moi-anh-em-tham.3747865/",
    "https://tinhte.vn/thread/vinfast-chinh-thuc-mo-coc-vf-7.3747695/",
]

# Khởi tạo danh sách để lưu dữ liệu
all_data = {'Tiêu đề': [], 'Nội dung': []}

for url in urls:
    driver.get(url)

    try: #cho mấy bài dạng article
        # Lấy tiêu đề bài báo
        title_element = driver.find_element(By.CSS_SELECTOR,"h1.jsx-89440")
        # driver.find_element(By.XPATH,"//input[@type='submit']").click()
        title = title_element.text.strip()

        # Lấy nội dung bài báo
        content_element = driver.find_element(By.CSS_SELECTOR,"article.jsx-89440 div.jsx-89440")
        content = content_element.text.strip()
    except: #cho mấy bài dạng fb post
        # Lấy tiêu đề bài báo
        title = driver.title

        # Lấy nội dung bài báo
        content_element = driver.find_element(By.CLASS_NAME, "xf-body-paragraph")
        content = content_element.text.strip()

    # In tiêu đề và nội dung ra console (kiểm tra)
    print("Tiêu đề:", title)
    print("Nội dung:", content)

    # Thêm dữ liệu vào danh sách
    all_data['Tiêu đề'].append(title)
    all_data['Nội dung'].append(content)

# Đóng trình duyệt
driver.quit()

# Tạo DataFrame từ dữ liệu
dataframe = pd.DataFrame(all_data)

# Xuất DataFrame ra file Excel
dataframe.to_excel('C:/The REST/Career/Automation Test/PyCharm_Python/Bài tập/Get data from article/tinhte_articles.xlsx', index=False)