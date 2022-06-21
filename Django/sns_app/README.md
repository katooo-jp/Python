## Django restframework & React Hooks

+ 仮想環境の作成・アクティベート
> `python -m venv venv`
> `source venv/bin/activate`

+ パッケージインストール
> `pip install django django-environ djangorestframework pillow`

+ DjangoProject作成
> `django-admin startproject config .`
> `python manage.py startapp アプリ名`

+ システム管理者作成
> `python manage.py createsuperuser`

+ DBマイグレーション
> `python manage.py makemigrations`
> `python manage.py migrate`

+ runserver起動
> `python manage.py runserver --settings config.local_settings`

+ React作成
> `npx create-react-app アプリ名`