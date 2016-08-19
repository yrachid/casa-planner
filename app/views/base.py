from flask import render_template
from flask.views import View


class ListView(View):

    template = 'default/list.html'

    '''
    An abstract pluggable Flask View for the Retrieve CRUD operation.

    CRUD views that will list content should extend this view and later
    be transformed to a view function through the as_view method from Flask
    View class.
    '''

    def get_objects(self):
        '''
        Method to specify how to return all objects retrieved from a datasource
        '''
        raise NotImplementedError()

    def get_template_name(self):
        '''
        Method to specify the template to be used as list rendering.
        '''
        return self.list_template

    def render(self, context):
        '''
        Template rendering function for this class.

        Works as a wrapper for the render_template Flask function.
        '''
        return render_template(
            self.template,
            **context
        )

    def dispatch_request(self):
        '''
        Method that will actually treat the request.

        This method will be used to transform this class into a view function.
        '''
        context = {'objects': self.get_objects()}
        return self.render(context)
