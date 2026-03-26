from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    about_text_1 = models.TextField()
    about_text_2 = models.TextField(blank=True, null=True)

    phone = models.CharField(max_length=20)
    email = models.EmailField()
    linkedin = models.URLField(blank=True, null=True)

    roles_count = models.CharField(max_length=50, blank=True, null=True, default='3+')
    career_start = models.CharField(max_length=50, blank=True, null=True, default='2023')
    leadership_text = models.CharField(max_length=100, blank=True, null=True, default='Team')
    focus_text = models.CharField(max_length=100, blank=True, null=True, default='Client')

    def __str__(self):
        return self.name


class Skill(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, help_text="Example: fas fa-users")
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.job_title} - {self.company}"


class Education(models.Model):
    institute = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    course = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.institute


class Language(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Hobby(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, help_text="Example: fas fa-plane-departure")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name