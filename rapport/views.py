from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
import datetime
from datetime import date


from evangelisation.utils import (get_stat_evang_person_infos, month_name, month_evang, month_numer,
    get_personne_evang_all_by__year, get_personne_evang_all_by_jour_and_mois_and_year, get_personne_evang_all_by_mois_and_year,
    get_personne_evang_by_jour_and_mois_and_year, get_personne_evang_by_mois_and_year, get_personne_evang_by_year,
    get_personne_total, get_stat_oui_jesus_by_mois)
from evangelisation.models import Evangelisation, Person

@login_required
def rapport_app_index(request):
    stat = None
    all_evang = []
    total = {}
    context = dict()
    liste_mois = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    if ('jour' and 'mois' and 'annee') in request.GET:
        jour = request.GET['jour']
        mois = request.GET['mois']
        annee = request.GET['annee']
        
        if jour == '----' and mois != '----' and annee != '----':
            context = get_stat_evang_person_infos(mois=month_numer(mois), year=annee)
            all_evang = get_personne_evang_all_by_mois_and_year(mois, annee)
            total = get_personne_total(all_evang)
            context['total'] = total
            context['all_evang'] = all_evang
        elif jour != '----' and mois != '----' and annee != '----':
            context = get_stat_evang_person_infos(jour=jour, mois=month_numer(mois), year=annee)
            all_evang = get_personne_evang_all_by_jour_and_mois_and_year(jour, mois, annee)
            total = get_personne_total(all_evang)
            context['total'] = total
            context['all_evang'] = all_evang
        elif jour == '----' and mois == '----' and annee != '----':
            context = get_stat_evang_person_infos(year=annee)
            all_evang = get_personne_evang_all_by__year(annee)
            total = get_personne_total(all_evang)
            liste_oui_by_mois = get_stat_oui_jesus_by_mois(all_evang)

            context['janvier_oui'] = liste_oui_by_mois[0]
            context['fevrier_oui'] = liste_oui_by_mois[1]
            context['mars_oui'] = liste_oui_by_mois[2]
            context['avril_oui'] = liste_oui_by_mois[3]
            context['mai_oui'] = liste_oui_by_mois[4]
            context['juin_oui'] = liste_oui_by_mois[5]
            context['juillet_oui'] = liste_oui_by_mois[6]
            context['aout_oui'] = liste_oui_by_mois[7]
            context['septembre_oui'] = liste_oui_by_mois[8]
            context['octobre_oui'] = liste_oui_by_mois[9]
            context['novembre_oui'] = liste_oui_by_mois[10]
            context['decembre_oui'] = liste_oui_by_mois[11]
            context['total'] = total
            context['all_evang'] = all_evang
            context['all'] = True
        elif jour == '----' and mois == '----' and annee == '----':
            try:
                context = get_stat_evang_person_infos(jour='----', mois='----', year='----')
                if context:
                    print(context)
                else:
                    context['error'] = True
            except ValueError:
                context['error'] = True
        elif jour != '----' and mois == '----' and annee == '----':
            try:
                context = get_stat_evang_person_infos(jour=jour, mois=mois, year=annee)
                if context:
                    print(context)
                else:
                    context['error'] = True
            except ValueError:
                context['error'] = True
        elif jour != '----' and mois != '----' and annee == '----':
            print("=========annee=====",'errorrrrrrrrrrr3333')
            try:
                context = get_stat_evang_person_infos(jour=jour, mois=mois, year=annee)
                if context:
                    print(context)
                else:
                    context['error'] = True
                    context['jour'] = jour
            except ValueError:
                context['error'] = True
                print("=========anneeexceptexcept=====",'errorrrrrrrrrrr3333')
        elif jour == '----' and mois != '----' and annee == '----':
            print("=========annee=====",'errorrrrrrrrrrr2222')
            try:
                context = get_stat_evang_person_infos(jour='----', mois=month_numer(mois), year='----')
                if context:
                    print(context)
                else:
                    context['error'] = True
            except ValueError:
                context['error'] = True
                print("=========annee except except=====",'errorrrrrrrrrrr2222')
        elif jour != '----' and mois == '----' and annee != '----':
            print("=========annee=====",'errorrrrrrrrrrr44444')
            try:
                context = get_stat_evang_person_infos(jour='----', mois=month_numer(mois), year='----')
                if context:
                    print(context)
                else:
                    context['error'] = True
            except ValueError:
                context['error'] = True
                print("=========annee except except=====",'errorrrrrrrrrrr44444')
    else:
        context = get_stat_evang_person_infos(autre=date.today().year)
        if context:
            print(context)
        else: 
            context['not_stat'] = True
        all_evang = get_personne_evang_all_by__year(date.today().year)
        total = get_personne_total(all_evang)
        liste_oui_by_mois = get_stat_oui_jesus_by_mois(all_evang)
        
        context['janvier_oui'] = liste_oui_by_mois[0]
        context['fevrier_oui'] = liste_oui_by_mois[1]
        context['mars_oui'] = liste_oui_by_mois[2]
        context['avril_oui'] = liste_oui_by_mois[3]
        context['mai_oui'] = liste_oui_by_mois[4]
        context['juin_oui'] = liste_oui_by_mois[5]
        context['juillet_oui'] = liste_oui_by_mois[6]
        context['aout_oui'] = liste_oui_by_mois[7]
        context['septembre_oui'] = liste_oui_by_mois[8]
        context['octobre_oui'] = liste_oui_by_mois[9]
        context['novembre_oui'] = liste_oui_by_mois[10]
        context['decembre_oui'] = liste_oui_by_mois[11]
        #===========+++END++++
        context['total'] = total
        context['annee'] = date.today().year
        context['all'] = True
        context['all_evang'] = all_evang
    context['select_link'] = 'rapport'
    return render(request, 'pages/rapport/index.html', context)




def rapport_app_detail(request, id):
    pass





















