from flask import Blueprint, render_template

view = Blueprint('view',__name__,template_folder='templates')

@view.route('/jquery/',methods=['GET'])
def jquery():
	return render_template('jquery/index.html',title='JQuery')

@view.route('/react/',methods=['GET'])
def react():
	return render_template('react/index.html',title='React.js')