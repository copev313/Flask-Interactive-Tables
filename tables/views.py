from tables import app
from tables.models import User
from flask import render_template, request


@app.route('/')
@app.route('/basic')
def index():
    users = User.query
    return render_template('basic_table.html',
                           title='Basic Table',
                           users=users)


@app.route('/server-side')
def server_side():
    return render_template('server_side_table.html',
                           title='Server-Driven Table')


@app.route('/api/data')
def data():
    query = User.query

    # Searching:
    search = request.args.get('search[value]')
    if search:
        query = query.filter(db.or_(
            User.name.like(f"%{search}%"),
            User.email.like(f"{search}%"),
        ))
    total_filtered = query.count()

    # Sorting:
    order = []
    i = 0

    while True:
        col_index = request.args.get(f"order[{i}][column]")
        if col_index is None:
            break

        col_name = request.args.get(f"columns[{col_index}][data]")
        if (col_name not in ['name', 'age', 'email']):
            col_name = 'name'

        descending = request.args.get(f"order[{i}][dir]") == 'desc'
        col = getattr(User, col_name)
        if descending:
            col = col.desc()

        order.append(col)
        i += 1

    if order:
        query = query.order_by(*order)

    # Pagination:
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    query = query.offset(start).limit(length)

    # Response:
    return {
        'data': [user.to_dict() for user in query],
        'recordsFiltered': total_filtered,
        'recordsTotal': User.query.count(),
        'draw': request.args.get('draw', type=int),
    }
