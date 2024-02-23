from .forms import CreatePostForm
from flask import render_template, request, Blueprint
from flask_login import login_required, current_user


site = Blueprint('site', __name__, template_folder='templates')


#create_post
@site.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = CreatePostForm()
    if request.method == 'POST' and form.validate_on_submit():
        img_url = form.img_url.data
        return f'{img_url}'
    else:
        return render_template('create_post.html', form=form)



#feed_route

#view_own_posts route

#edit_route



#delete_post_route

