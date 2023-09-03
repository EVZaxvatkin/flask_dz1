from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/clothes/')
def clothes():
    head = {
        'type': 'Ассортимент',
        'size': 'Размер',
        'price': 'Цена'
    }

    clothes_list = [
        {
            'type': 'Футболка',
            'size': '42-50',
            'price': '500 руб.'
        },
        {
            'type': 'Шорты',
            'size': '42-50',
            'price': '600 руб.'
        },
        {
            'type': 'Спортивные штаны',
            'size': '42-50',
            'price': '800 руб.'
        }
    ]
    return render_template('clothes.html', **head, clothes_list=clothes_list)


@app.route('/shoes/')
def shoes():
    head = {
        'type': 'Ассортимент',
        'size': 'Размер',
        'price': 'Цена'
    }

    shoes_list = [
        {
            'type': 'Кроссовки',
            'size': '41-46',
            'price': '3500 руб.'
        },
        {
            'type': 'Мужские туфли',
            'size': '41-46',
            'price': '4500 руб.'
        },
        {
            'type': 'Женские туфли',
            'size': '35-39',
            'price': '4000 руб.'
        }
    ]
    return render_template('shoes.html', **head, shoes_list=shoes_list)

@app.route('/jackets/')
def jackets():
    head = {
        'type': 'Ассортимент',
        'size': 'Размер',
        'price': 'Цена'
    }

    jackets_list = [
        {
            'type': 'Мужская куртка',
            'size': '44-56',
            'price': '5000 руб.'
        },
        {
            'type': 'Женская крутка',
            'size': '40-52',
            'price': '5000 руб.'
        },
        {
            'type': 'Детские куртки',
            'size': '32-40',
            'price': '3500 руб.'
        }
    ]
    return render_template('jackets.html', **head, jackets_list=jackets_list)

if __name__ == '__main__':
    app.run(debug=True)