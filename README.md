# 📝 Django Form App

This is my **first Django project** — a simple form-based web application that allows users to submit their personal information including a profile photo. 
The submitted data is stored in a database and displayed in the Django admin panel.

## 🔧 Tech Stack

- **Backend:** Django
- **Frontend:** HTML, Bootstrap 5
- **Database:** SQLite (default Django DB)
- **File Uploads:** Stored in `/media/files/`

## 📸 Screenshots

### 🖥️ Form Page
![Form Page](formpage_screenshot.png)![Form_Screenshot](https://github.com/user-attachments/assets/ab1d46ce-3f84-4e48-97fc-b906707f7fea)


### 🗃️ Database Entry
![Database Entry]![database screenshot](https://github.com/user-attachments/assets/688a54b4-e8ad-46ba-a489-c0a903af4293)


## 📂 Project Structure

- **formpage.html** – Bootstrap-styled form with fields like name, email, age, gender, address, and profile photo.
- **views.py** – Handles form submission, saves data to the model, and redirects to a thank-you page.
- **models.py** – Defines the `person` model with fields including a `FileField` for profile uploads.

## 🧠 Features

- Form submission with CSRF protection
- File upload functionality for profile photo
- Server-side data validation
- Thank-you page redirection after successful submission
- Auto-timestamp for each submission

## 🛠️ How to Run

```bash
git clone https://github.com/yourusername/django-form-app.git
cd django-form-app
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
