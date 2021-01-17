    #db.drop_all()
    #db.create_all()
    db.session.add(User(username="Flask", test = "",email="example1@example.com",preferances="American, Chineses, Thai",firbase_id="1"))
    db.session.commit()

    users = User.query.all()
    print(users)
    #app.run()
    manager.run()

    with app.app_context():
        if db.engine.url.drivername == 'sqlite':
            migrate.init_app(app, db, render_as_batch=True)
        else:
            migrate.init_app(app, db)

