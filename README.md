<h3>
API to create smart-contracts and mint NFT
</h3>

<h3>
Stack
</h3>

<ul>
<li>
Python 3.10
</li>
<li>
PostgreSQL
</li>
<li>
Docker
</li>
</ul>

<h3>
Libraries
</h3>

All dependencies you can see in `requirements.txt`

`Django==4.0.4`

`djangorestframework==3.13.1`

`web3==5.28.0`

<h3>Postman</h3>

All requests and routes was tested with Postman

`/tokens/create/` use "POST" method to create new token

`/tokens/list/` use "GET" method to get all token

`/tokens/list/<int:pk>` use "GET" method to get token by pk

`/tokens/total_supply/` use "GET" method to get amount of tokens


<h3>Launch</h3>

Use `git clone https://github.com/rogaliiik/web3_contracts.git`

Install dependecies with `pip install -r requirements.txt`

Start server with `python manage.py runserver`


