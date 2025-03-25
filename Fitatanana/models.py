from django.db import models
from datetime import date
# Create your models here.
#-----------------------------------------------------------------------------------------------------------------------
"""
   Efa Mety Miasa
"""
class Mpino3(models.Model):
    LAHY = "L"
    VAVY = "V"
    l_v = [
        (LAHY,"Lahy"),
        (VAVY,"Vavy")
    ]
    Mpadray = "P"
    Kristianina = "K"
    m_p = [
        (Mpadray,"Mpadray"),
        (Kristianina,"Kristianina")
    ]

    ENY = "ENY"
    TSY = "TSY"
    b_t = [
        (ENY,"ENY"),
        (TSY,"TSY")
    ]
    LaharanaKaratra = models.CharField(max_length=100,verbose_name="Laharan'ny Karatra")
    Anarana = models.CharField(max_length=250)
    Fanampiny = models.CharField(max_length=255)
    Teraka = models.PositiveIntegerField()
    Taona = models.IntegerField(null=True,blank=True)
    #ToheranaNahaterahana = models.CharField(null=True,max_length=250)
    L_v = models.CharField(max_length=1,choices=l_v)
    Antonasa = models.CharField(max_length=200)
    #Rainy = models.CharField(max_length=400)
    #Reny = models.CharField(max_length=400)
    Adresy = models.CharField(max_length=255)
    Faritra = models.CharField(max_length=150)
    Fiday = models.CharField(max_length=13,null=True)

    TaonaNahatogavanaTaoAmpiagonana = models.IntegerField(null=True,default=0)
    FiagonanaNiavina = models.CharField(blank=True,null=True,max_length=250)

    batisa = models.CharField(max_length=3,choices=b_t)
    taona_nanaovana_batysa =  models.IntegerField(null=True,blank=True)

    M_P = models.CharField(max_length=1,choices=m_p)
    TaonaNahaMpandray = models.IntegerField(blank=True, null=True,default=0)
    #Sampana = models.CharField(blank=True, max_length=250,null=True,default="")
    DatyNakanaKaratra = models.CharField(null=True,max_length=20)

    def taona(self):
        if self.Teraka:
            adroany = date.today()
            taona = adroany.year - self.Teraka
            #if (adroany.month, adroany.day) < (self.Teraka.month,self.Teraka.year):
            #    taona -1
            return taona
        return None
    def save(self,*args,**kwargs ):
        self.Taona = self.taona()
        super().save(*args,**kwargs)

    def __str__(self):
        #return str
        return self.Anarana

class Adidy(models.Model):
    Mpino = models.ForeignKey(Mpino3, on_delete=models.DO_NOTHING)
    Taona = models.IntegerField(default=2025)

    J = models.IntegerField(default=0)
    P_J = models.IntegerField(default=0)
    J_Date = models.DateField(blank=True,null=True)

    F = models.IntegerField(default=0)
    P_F = models.IntegerField(default=0)
    F_Date = models.DateField(blank=True,null=True)

    M = models.IntegerField(default=0)
    P_M = models.IntegerField(default=0)
    M_Date = models.DateField(blank=True,null=True)

    Av = models.IntegerField(default=0)
    P_Av = models.IntegerField(default=0)
    Av_Date = models.DateField(blank=True,null=True)

    Ma = models.IntegerField(default=0)
    P_Ma = models.IntegerField(default=0)
    Ma_Date = models.DateField(blank=True,null=True)

    Ji = models.IntegerField(default=0)
    P_Ji = models.IntegerField(default=0)
    Ji_Date = models.DateField(blank=True,null=True)

    Ju = models.IntegerField(default=0)
    P_Ju = models.IntegerField(default=0)
    Ju_Date = models.DateField(blank=True,null=True)

    Ag = models.IntegerField(default=0)
    P_Ag = models.IntegerField(default=0)
    Ag_Date = models.DateField(blank=True,null=True)

    S = models.IntegerField(default=0)
    P_S = models.IntegerField(default=0)
    S_Date = models.DateField(blank=True,null=True)

    Ak = models.IntegerField(default=0)
    P_Ak = models.IntegerField(default=0)
    Ac_Date = models.DateField(blank=True,null=True)

    N = models.IntegerField(default=0)
    P_N = models.IntegerField(default=0)
    N_Date = models.DateField(blank=True,null=True)

    D = models.IntegerField(default=0)
    P_D = models.IntegerField(default=0)
    D_Date = models.DateField(blank=True,null=True)

    Fitabarany = models.IntegerField(null=True,blank=True)

    #-----------------------------------------------------
    #-----------------------------------------------------
    def __str__(self):
        return self.Mpino.__str__()

    def save(self, *args, **kwargs):
        self.Fitabarany = sum([self.J,self.P_J,self.F,self.P_F,self.M,self.P_M,self.Av,self.P_Av,
                               self.Ma,self.P_Ma,self.Ji,self.P_Ji,self.Ju,self.P_Ju,self.Ag,self.P_Ag,
                               self.S,self.P_S,self.Ak,self.P_Ak,self.N,self.P_N,self.D,self.P_D])

        super(Adidy,self).save(*args, **kwargs)

    def total(self):
        return 12

class Katekomen(models.Model):
    Mpino =  Mpino = models.ForeignKey(Mpino3, on_delete=models.CASCADE, related_name='Mpino')
    Taompianarana = models.PositiveIntegerField()
    Daty_Nidirana = models.DateField()


class Fanamarihana(models.Model):
    F_Mpino =  models.ForeignKey(Mpino3, on_delete=models.CASCADE, related_name='F_Mpino')
    Lohanteny = models.CharField(blank=True,null=True,max_length=250)
    Fanamarihana = models.TextField(blank=True,null=True,max_length=3000)