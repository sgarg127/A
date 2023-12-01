from django.contrib.auth.base_user import BaseUserManager 


class UserManager(BaseUserManager):

    def create_user(self,email,username,phone_number,password=None):
        if not email:
            raise ValueError('Email is required')
        if not username:
            raise ValueError('Username is required')
        if not phone_number:
            raise ValueError('phone number is required')
        
        user=self.model(email=self.normalize_email(email),
                        username=username,
                        phone_number=phone_number)

        user.set_password(password)
        user.save(using=self.db)

        return user 
    
    def create_superuser(self,email,username,phone_number,password):

        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
            password=password)
        
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True

        user.save(using=self.db)
        return user 
    
    def create_admin(self,email,username,phone_number,password):

        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
            password=password)
        
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=False

        user.save(using=self.db)
        return user 
    #just to check if working 

    def create_manager(self,email,username,phone_number,password):

        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
            password=password)
        
        user.is_admin=False 
        user.is_staff=True
        user.is_superuser=False

        user.save(using=self.db)
        return user 