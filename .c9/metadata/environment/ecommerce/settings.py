{"filter":false,"title":"settings.py","tooltip":"/ecommerce/settings.py","undoManager":{"mark":82,"position":82,"stack":[[{"start":{"row":146,"column":0},"end":{"row":153,"column":16},"action":"remove","lines":["EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'","","","EMAIL_USE_TLS = True ","EMAIL_HOST = 'smtp.gmail.com'","EMAIL_HOST_USER = os.environ.get(\"lamrini788@gmail.com\")","EMAIL_HOST_PASSWORD = os.environ.get(\"EMAIL_PASSWORD\")","EMAIL_PORT = 587"],"id":235}],[{"start":{"row":137,"column":0},"end":{"row":137,"column":4},"action":"remove","lines":["    "],"id":236}],[{"start":{"row":137,"column":0},"end":{"row":137,"column":63},"action":"insert","lines":["STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')"],"id":237}],[{"start":{"row":137,"column":63},"end":{"row":138,"column":0},"action":"insert","lines":["",""],"id":238}],[{"start":{"row":136,"column":5},"end":{"row":137,"column":63},"action":"remove","lines":["","STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')"],"id":239}],[{"start":{"row":13,"column":11},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":240}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":22},"action":"insert","lines":["import dj_database_url"],"id":241}],[{"start":{"row":84,"column":0},"end":{"row":84,"column":1},"action":"insert","lines":["#"],"id":242}],[{"start":{"row":84,"column":1},"end":{"row":84,"column":2},"action":"insert","lines":[" "],"id":243}],[{"start":{"row":85,"column":3},"end":{"row":85,"column":4},"action":"insert","lines":["#"],"id":244}],[{"start":{"row":86,"column":6},"end":{"row":86,"column":7},"action":"insert","lines":["#"],"id":245}],[{"start":{"row":87,"column":5},"end":{"row":87,"column":6},"action":"remove","lines":[" "],"id":246}],[{"start":{"row":87,"column":5},"end":{"row":87,"column":6},"action":"insert","lines":["#"],"id":247}],[{"start":{"row":88,"column":3},"end":{"row":88,"column":4},"action":"insert","lines":["#"],"id":248}],[{"start":{"row":89,"column":0},"end":{"row":89,"column":1},"action":"insert","lines":["#"],"id":249}],[{"start":{"row":89,"column":2},"end":{"row":90,"column":0},"action":"insert","lines":["",""],"id":250},{"start":{"row":90,"column":0},"end":{"row":90,"column":1},"action":"insert","lines":["D"]},{"start":{"row":90,"column":1},"end":{"row":90,"column":2},"action":"insert","lines":["A"]},{"start":{"row":90,"column":2},"end":{"row":90,"column":3},"action":"insert","lines":["T"]},{"start":{"row":90,"column":3},"end":{"row":90,"column":4},"action":"insert","lines":["A"]}],[{"start":{"row":90,"column":0},"end":{"row":90,"column":4},"action":"remove","lines":["DATA"],"id":251},{"start":{"row":90,"column":0},"end":{"row":90,"column":9},"action":"insert","lines":["DATABASES"]}],[{"start":{"row":90,"column":9},"end":{"row":90,"column":10},"action":"insert","lines":[" "],"id":252},{"start":{"row":90,"column":10},"end":{"row":90,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":90,"column":11},"end":{"row":90,"column":12},"action":"insert","lines":[" "],"id":253}],[{"start":{"row":90,"column":12},"end":{"row":90,"column":13},"action":"insert","lines":["{"],"id":254}],[{"start":{"row":90,"column":13},"end":{"row":92,"column":1},"action":"insert","lines":["","    ","}"],"id":255}],[{"start":{"row":91,"column":4},"end":{"row":91,"column":6},"action":"insert","lines":["''"],"id":256}],[{"start":{"row":91,"column":5},"end":{"row":91,"column":6},"action":"insert","lines":["d"],"id":257},{"start":{"row":91,"column":6},"end":{"row":91,"column":7},"action":"insert","lines":["e"]},{"start":{"row":91,"column":7},"end":{"row":91,"column":8},"action":"insert","lines":["a"]},{"start":{"row":91,"column":8},"end":{"row":91,"column":9},"action":"insert","lines":["u"]},{"start":{"row":91,"column":9},"end":{"row":91,"column":10},"action":"insert","lines":["k"]}],[{"start":{"row":91,"column":9},"end":{"row":91,"column":10},"action":"remove","lines":["k"],"id":258},{"start":{"row":91,"column":8},"end":{"row":91,"column":9},"action":"remove","lines":["u"]},{"start":{"row":91,"column":7},"end":{"row":91,"column":8},"action":"remove","lines":["a"]}],[{"start":{"row":91,"column":7},"end":{"row":91,"column":8},"action":"insert","lines":["f"],"id":259},{"start":{"row":91,"column":8},"end":{"row":91,"column":9},"action":"insert","lines":["a"]},{"start":{"row":91,"column":9},"end":{"row":91,"column":10},"action":"insert","lines":["u"]},{"start":{"row":91,"column":10},"end":{"row":91,"column":11},"action":"insert","lines":["l"]},{"start":{"row":91,"column":11},"end":{"row":91,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":91,"column":13},"end":{"row":91,"column":14},"action":"insert","lines":[":"],"id":260}],[{"start":{"row":91,"column":14},"end":{"row":91,"column":15},"action":"insert","lines":[" "],"id":261}],[{"start":{"row":91,"column":15},"end":{"row":91,"column":16},"action":"insert","lines":["d"],"id":262},{"start":{"row":91,"column":16},"end":{"row":91,"column":17},"action":"insert","lines":["j"]}],[{"start":{"row":91,"column":15},"end":{"row":91,"column":17},"action":"remove","lines":["dj"],"id":263},{"start":{"row":91,"column":15},"end":{"row":91,"column":30},"action":"insert","lines":["dj_database_url"]}],[{"start":{"row":91,"column":30},"end":{"row":91,"column":31},"action":"insert","lines":["."],"id":264},{"start":{"row":91,"column":31},"end":{"row":91,"column":32},"action":"insert","lines":["p"]},{"start":{"row":91,"column":32},"end":{"row":91,"column":33},"action":"insert","lines":["a"]},{"start":{"row":91,"column":33},"end":{"row":91,"column":34},"action":"insert","lines":["s"]},{"start":{"row":91,"column":34},"end":{"row":91,"column":35},"action":"insert","lines":["r"]}],[{"start":{"row":91,"column":34},"end":{"row":91,"column":35},"action":"remove","lines":["r"],"id":265},{"start":{"row":91,"column":33},"end":{"row":91,"column":34},"action":"remove","lines":["s"]}],[{"start":{"row":91,"column":33},"end":{"row":91,"column":34},"action":"insert","lines":["r"],"id":266},{"start":{"row":91,"column":34},"end":{"row":91,"column":35},"action":"insert","lines":["s"]},{"start":{"row":91,"column":35},"end":{"row":91,"column":36},"action":"insert","lines":["e"]}],[{"start":{"row":91,"column":36},"end":{"row":91,"column":38},"action":"insert","lines":["()"],"id":267}],[{"start":{"row":91,"column":37},"end":{"row":91,"column":38},"action":"insert","lines":["o"],"id":268},{"start":{"row":91,"column":38},"end":{"row":91,"column":39},"action":"insert","lines":["s"]},{"start":{"row":91,"column":39},"end":{"row":91,"column":40},"action":"insert","lines":["."]},{"start":{"row":91,"column":40},"end":{"row":91,"column":41},"action":"insert","lines":["e"]},{"start":{"row":91,"column":41},"end":{"row":91,"column":42},"action":"insert","lines":["n"]}],[{"start":{"row":91,"column":40},"end":{"row":91,"column":42},"action":"remove","lines":["en"],"id":269},{"start":{"row":91,"column":40},"end":{"row":91,"column":47},"action":"insert","lines":["environ"]}],[{"start":{"row":91,"column":47},"end":{"row":91,"column":48},"action":"insert","lines":["."],"id":270},{"start":{"row":91,"column":48},"end":{"row":91,"column":49},"action":"insert","lines":["g"]},{"start":{"row":91,"column":49},"end":{"row":91,"column":50},"action":"insert","lines":["e"]},{"start":{"row":91,"column":50},"end":{"row":91,"column":51},"action":"insert","lines":["t"]}],[{"start":{"row":91,"column":48},"end":{"row":91,"column":51},"action":"remove","lines":["get"],"id":271},{"start":{"row":91,"column":48},"end":{"row":91,"column":53},"action":"insert","lines":["get()"]}],[{"start":{"row":91,"column":52},"end":{"row":91,"column":54},"action":"insert","lines":["''"],"id":272}],[{"start":{"row":91,"column":53},"end":{"row":91,"column":54},"action":"insert","lines":["D"],"id":273},{"start":{"row":91,"column":54},"end":{"row":91,"column":55},"action":"insert","lines":["A"]},{"start":{"row":91,"column":55},"end":{"row":91,"column":56},"action":"insert","lines":["T"]},{"start":{"row":91,"column":56},"end":{"row":91,"column":57},"action":"insert","lines":["B"]},{"start":{"row":91,"column":57},"end":{"row":91,"column":58},"action":"insert","lines":["A"]},{"start":{"row":91,"column":58},"end":{"row":91,"column":59},"action":"insert","lines":["S"]},{"start":{"row":91,"column":59},"end":{"row":91,"column":60},"action":"insert","lines":["E"]},{"start":{"row":91,"column":60},"end":{"row":91,"column":61},"action":"insert","lines":["_"]}],[{"start":{"row":91,"column":61},"end":{"row":91,"column":62},"action":"insert","lines":["U"],"id":274},{"start":{"row":91,"column":62},"end":{"row":91,"column":63},"action":"insert","lines":["R"]},{"start":{"row":91,"column":63},"end":{"row":91,"column":64},"action":"insert","lines":["L"]}],[{"start":{"row":24,"column":13},"end":{"row":24,"column":65},"action":"remove","lines":["'&3bu_88ep+^iq@iolrmx4m^6j#+z&!!&bu2y*vqu=dsm90_oox'"],"id":275},{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":["'"]},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"insert","lines":[";"]}],[{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"remove","lines":[";"],"id":276}],[{"start":{"row":24,"column":14},"end":{"row":24,"column":16},"action":"insert","lines":["''"],"id":277}],[{"start":{"row":24,"column":14},"end":{"row":24,"column":16},"action":"remove","lines":["''"],"id":278}],[{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"insert","lines":["S"],"id":279},{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":["E"]},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["C"]}],[{"start":{"row":24,"column":14},"end":{"row":24,"column":17},"action":"remove","lines":["SEC"],"id":280},{"start":{"row":24,"column":14},"end":{"row":24,"column":24},"action":"insert","lines":["SECRET_KEY"]}],[{"start":{"row":24,"column":24},"end":{"row":24,"column":25},"action":"insert","lines":["'"],"id":281}],[{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":["o"],"id":282},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"insert","lines":["s"]},{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":["."]},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"remove","lines":["e"],"id":283},{"start":{"row":24,"column":16},"end":{"row":24,"column":23},"action":"insert","lines":["environ"]}],[{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"insert","lines":["."],"id":284},{"start":{"row":24,"column":24},"end":{"row":24,"column":25},"action":"insert","lines":["g"]},{"start":{"row":24,"column":25},"end":{"row":24,"column":26},"action":"insert","lines":["e"]},{"start":{"row":24,"column":26},"end":{"row":24,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":24,"column":24},"end":{"row":24,"column":27},"action":"remove","lines":["get"],"id":285},{"start":{"row":24,"column":24},"end":{"row":24,"column":29},"action":"insert","lines":["get()"]}],[{"start":{"row":24,"column":29},"end":{"row":24,"column":41},"action":"remove","lines":["'SECRET_KEY'"],"id":286}],[{"start":{"row":24,"column":28},"end":{"row":24,"column":40},"action":"insert","lines":["'SECRET_KEY'"],"id":287}],[{"start":{"row":91,"column":4},"end":{"row":91,"column":5},"action":"insert","lines":["^"],"id":288},{"start":{"row":91,"column":5},"end":{"row":91,"column":6},"action":"insert","lines":["^"]}],[{"start":{"row":91,"column":5},"end":{"row":91,"column":6},"action":"remove","lines":["^"],"id":289},{"start":{"row":91,"column":4},"end":{"row":91,"column":5},"action":"remove","lines":["^"]}],[{"start":{"row":91,"column":4},"end":{"row":91,"column":5},"action":"insert","lines":[")"],"id":290}],[{"start":{"row":91,"column":4},"end":{"row":91,"column":5},"action":"remove","lines":[")"],"id":291}],[{"start":{"row":91,"column":4},"end":{"row":91,"column":5},"action":"insert","lines":["("],"id":292}],[{"start":{"row":91,"column":4},"end":{"row":91,"column":5},"action":"remove","lines":["("],"id":293}],[{"start":{"row":91,"column":56},"end":{"row":91,"column":57},"action":"insert","lines":["A"],"id":294}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":["i"],"id":295},{"start":{"row":15,"column":1},"end":{"row":15,"column":2},"action":"insert","lines":["m"]},{"start":{"row":15,"column":2},"end":{"row":15,"column":3},"action":"insert","lines":["p"]},{"start":{"row":15,"column":3},"end":{"row":15,"column":4},"action":"insert","lines":["o"]},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["r"]},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":[" "],"id":296},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["d"]},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["j"]},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["a"]},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["n"]},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["g"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["o"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["_"]}],[{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"remove","lines":["_"],"id":297}],[{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":[","],"id":298},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["c"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["o"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["r"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"remove","lines":["e"],"id":299},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"remove","lines":["r"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"remove","lines":["o"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"remove","lines":["c"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"remove","lines":[","]}],[{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["."],"id":300},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["c"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["o"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["r"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["e"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["."]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["w"]},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["g"],"id":301},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["i"]}],[{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":[" "],"id":302}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":6},"action":"remove","lines":["import"],"id":303},{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":["f"]},{"start":{"row":15,"column":1},"end":{"row":15,"column":2},"action":"insert","lines":["r"]},{"start":{"row":15,"column":2},"end":{"row":15,"column":3},"action":"insert","lines":["o"]},{"start":{"row":15,"column":3},"end":{"row":15,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["i"],"id":304},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["m"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":["p"]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["o"]},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":["r"]},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":[" "],"id":305}],[{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["g"],"id":306},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["e"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":29},"end":{"row":15,"column":32},"action":"remove","lines":["get"],"id":307},{"start":{"row":15,"column":29},"end":{"row":15,"column":51},"action":"insert","lines":["get_wsgi_application()"]}],[{"start":{"row":15,"column":49},"end":{"row":15,"column":51},"action":"remove","lines":["()"],"id":308}],[{"start":{"row":14,"column":22},"end":{"row":15,"column":49},"action":"remove","lines":["","from django.core.wsgi import get_wsgi_application"],"id":309}],[{"start":{"row":40,"column":29},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":310},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":6},"action":"insert","lines":["''"],"id":311}],[{"start":{"row":41,"column":5},"end":{"row":41,"column":6},"action":"insert","lines":["d"],"id":312},{"start":{"row":41,"column":6},"end":{"row":41,"column":7},"action":"insert","lines":["j"]},{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"insert","lines":["a"]},{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"insert","lines":["n"]}],[{"start":{"row":41,"column":9},"end":{"row":41,"column":10},"action":"insert","lines":["g"],"id":313},{"start":{"row":41,"column":10},"end":{"row":41,"column":11},"action":"insert","lines":["o"]},{"start":{"row":41,"column":11},"end":{"row":41,"column":12},"action":"insert","lines":["_"]}],[{"start":{"row":41,"column":12},"end":{"row":41,"column":13},"action":"insert","lines":["t"],"id":314},{"start":{"row":41,"column":13},"end":{"row":41,"column":14},"action":"insert","lines":["o"]},{"start":{"row":41,"column":14},"end":{"row":41,"column":15},"action":"insert","lines":["d"]},{"start":{"row":41,"column":15},"end":{"row":41,"column":16},"action":"insert","lines":["o"]}],[{"start":{"row":41,"column":17},"end":{"row":41,"column":18},"action":"insert","lines":[","],"id":315}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":18},"action":"remove","lines":["'django_todo',"],"id":316},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"remove","lines":["    "]},{"start":{"row":40,"column":29},"end":{"row":41,"column":0},"action":"remove","lines":["",""]},{"start":{"row":40,"column":28},"end":{"row":40,"column":29},"action":"remove","lines":[","]}],[{"start":{"row":40,"column":28},"end":{"row":40,"column":29},"action":"insert","lines":[","],"id":317}]]},"ace":{"folds":[],"scrolltop":206.5,"scrollleft":0,"selection":{"start":{"row":40,"column":29},"end":{"row":40,"column":29},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":12,"state":"start","mode":"ace/mode/python"}},"timestamp":1564769854462,"hash":"240075dcb6487b78a20296cb5d16e8b9dc4cbacc"}