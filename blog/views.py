from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Billet
from .models import Equipement
from .models import Character
from .forms import MoveForm


 
 
def post_list(request):
    billets = Billet.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'billets': billets})

def post_detail(request, pk):
    billet = get_object_or_404(Billet, pk=pk)
    return render(request, 'blog/post_detail.html', {'billet': billet})

def ch_list(request):
    characters = Character.objects.all()
    equipements = Equipement.objects.all()
    return render(request, 'blog/ch_list.html', {'characters': characters, 'equipements': equipements} )

def eq_list(request):
    equipements = Equipement.objects.all()
    return render(request, 'blog/eq_list.html', {'equipements': equipements})

def character_detail(request, id_character):
    character = get_object_or_404(Character, id_character=id_character)
    ancien_lieu = character.lieu
    if request.method == 'POST':
        form = MoveForm(request.POST, instance=character)
        if form.is_valid():
            updated_character = form.save(commit=False)

            if (updated_character.lieu != ancien_lieu and (updated_character.lieu.disponibilite == "libre" or updated_character.lieu.id_equip == "Hall")) and ((updated_character.etat == "Horreur" and updated_character.lieu.id_equip == "Conjuring") or (updated_character.etat == "Space Opera" and updated_character.lieu.id_equip == "Star Wars") or (updated_character.etat == "Fantasy" and updated_character.lieu.id_equip == "Le seigneur des anneaux") or (updated_character.lieu.id_equip == "Hall")):

                ancien_lieu.disponibilite = "libre"
                ancien_lieu.save()

                updated_character.lieu.disponibilite = "En diffusion"
                updated_character.etat = "Satisfait" 
                updated_character.lieu.save()

                if updated_character.lieu.id_equip == "Hall":
                    updated_character.lieu.disponibilite = "libre"
                    updated_character.save()

                updated_character.save()

                return redirect('character_detail', id_character=id_character)
            else:
                form.add_error('lieu', 'Le changement n\'est pas possible')
    else:
        form = MoveForm(instance=character)

    return render(request, 'blog/character_detail.html', {'character': character, 'form': form})
