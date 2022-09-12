## Запуск
1. Устанавливаем git и docker  
`sudo apt install git docker.io -y`
2. Копируем репозиторий в рабочую директорию  
`git clone https://github.com/Kit1001/test_stripe.git`
3. Переходим в папку проекта  
`cd test_stripe`  
4. Создаем образ из файлов проекта  
`sudo docker build . -t teststripe`  
5. Создаем и запускаем контейнер из полученного образа  
`sudo docker run -d -p 80:80 --env-file keys.env teststripe`

### Выполненные задачи:
1. Django Модель Item с полями (name, description, price)  
2. GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item
3. GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy
4. Залить решение на Github, описать запуск в Readme.md
5. Опубликовать свое решение чтобы его можно было быстро и легко протестировать
6. Запуск используя Docker
7. Использование environment variables
8. Просмотр Django Моделей в Django Admin панели
9. Запуск приложения на удаленном сервере
10. Модель Order, в которой можно объединить несколько Item
11. Модели Discount, Tax, которые можно прикрепить к модели Order

#### Не выполнил:
1. Добавить поле Item.currency,создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
2. Реализовать не Stripe Session, а Stripe Payment Intent.