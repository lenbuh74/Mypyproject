# Интернет-магазин Бухмастовой Елены, группа М3110 

В поисках идеи для проекта я подумала, что моя тетя, занимаясь созданием украшений из стекла и шерсти ручной работы, столкнулась с проблемой отсутствия информационного ресурса для распространения товара. Поэтому я решила разработать для нее интернет-магазин. 

#### В ходе создания магазина я преследовала следующие задачи: 
1. Создать каталог товаров, корзину покупателя, систему скидок, отзывов 
2. Разработать систему администрирования заказов 
3. Интегрировать систему оплаты 
4. Создать систему регистрации пользователей и личный кабинет для просмотра истории заказов 
5. Осуществить функцию обратной связи 
6. Реализовать систему информирования о выполняемых пользователем действий по email 

#### Для их достижения я использовала следующие технологии: 
1. Django 1.10.6 
2. Библиотеки Pillow, registration 
3. Платежная система paypal 
4. Очередь задач Celery 
5. Фреймворк Bootstrap 

## Описание проекта: 
Пользователь попадает в каталог товаров. Он может просмотреть все украшения, а также ознакомиться с продукцией по категориям. Щелкнув на нужный товар, покупатель может посмотреть его описание, оставить свои отзывы о данной продукции или продавце, а также добавить нужное количество в корзину, после чего может применить скидочные коды (в случае их действия стоимость конечного заказа уменьшается), продолжить шоппинг или перейти на страницу оформления заказа. Для оформления заказа пользователь заполняет свои личные данные и переходит на страницу оплаты, на указанный адрес электронной почты приходит сообщение с номером заказа. В случае успешной оплаты, пользователь получает по почте детали своего заказа. На странице обратной связи покупатель может отправить свои отзывы, вопросы, жалобы и предложения продавцу. Если клиент заказывает украшения не в первый раз и хочет отслеживать историю своих заказов, то он может зарегистрироваться по соответствующей ссылке и в случае подтверждения своего аккаунта (ссылку он получит по электронной почте) попадет в личный кабинет, где собраны детали о всех его заказах с возможностью распечатать их. Если магазин понравился клиенту, то он может рассказать о нем в социальных сетях. 

Все данные отображаются в базе данных SQLite, а также в панели администрирования, где продавец может редактировать данные, отслеживать заказы, экспортировать детали заказов и сохранять их в формате SCV. 

### С интерфейсом проекта Вы можете ознакомиться по прикрепленным изображением ниже:

#### Каталог товаров 

![alt text](https://cloud.githubusercontent.com/assets/22623962/26783051/ed0b7538-49fe-11e7-8c2d-30524f3ed846.jpg)


#### Личный кабинет и детали одного из заказов 

![alt text](https://cloud.githubusercontent.com/assets/22623962/26783720/5bbbdfb0-4a02-11e7-8786-906df4ba20a8.jpg)

![alt text](https://cloud.githubusercontent.com/assets/22623962/26783780/b475280a-4a02-11e7-80bd-6aa333e1c858.jpg)



#### Форма обратной связи 

![alt text](https://cloud.githubusercontent.com/assets/22623962/26783986/c08021bc-4a03-11e7-9ef6-242eb9e0e1e6.jpg)



#### Описание товара, отзывы

![alt text](https://cloud.githubusercontent.com/assets/22623962/26783511/4a17e584-4a01-11e7-9703-52f2a08c0306.jpg)



#### Корзина покупателя 

![alt text](https://cloud.githubusercontent.com/assets/22623962/26783639/df84b552-4a01-11e7-9f3b-6ac06c9f0eef.jpg)



#### Оформление заказа 

![alt text]()

