from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class ThankYouView(TemplateView):
    template_name =  'pages/thankyou.html'
    def get(self, request, *args, **kwargs):
        context = {"message": "Hello!"}
        return self.render_to_response(context)