from django.core.exceptions import ValidationError

class Players(models.Model):
  username = models.CharField(max_length = 30)
  password = models.CharField(max_length = 30)
  email = models.CharField(max_length = 50)
  created_at = models.DateTimeField('date created')

  def clean(self):
    if(len(self.password) < 8):
      raise ValidationError("password too short") 
    email_validator = re.compile('^[A-Z0-9-.]+[a-z0-9-]+[a-zA-Z]{4,}$')
    if(email_validator.match(self.email) == None):
      raise ValidationError("invalid email")

  def save(self, **kwargs):
    self.full_clean()
    return super(Players, self).save(**kwargs)

class Heroes(models.Model):
  player = ForeignKey(Players)
  name = models.CharField(max_length = 20)
  type = models.CharField()
  strength = models.IntegerField(default=10)
  
class Teams(models.Model):
  name = models.CharField()
  heroes = ManyToManyField(Hero)