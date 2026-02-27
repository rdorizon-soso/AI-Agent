#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Echo Prénom

Description:
    Affiche un message de salutation avec le prénom fourni en argument de ligne de commande.
    Ce script démontre la gestion des arguments CLI avec argparse et la validation des entrées.

Usage:
    python script.py <prénom>

Exemples:
    python script.py Jean
    python script.py José
    python script.py Jean-Pierre
    python script.py "O'Connor"
    python script.py -h

Author: Développeur
Date: 16 février 2026
Version: 1.0
"""

import argparse
import sys


def valider_prenom(prenom):
    """
    Valide que le prénom n'est pas vide ou ne contient que des espaces.
    
    Cette fonction vérifie que le prénom fourni est valide (non-vide et
    contient au moins un caractère non-espace). Elle retourne le prénom
    nettoyé des espaces superflus.
    
    Args:
        prenom (str): Le prénom à valider
    
    Raises:
        SystemExit: Quitte le programme avec le code 1 si la validation échoue
    
    Returns:
        str: Le prénom validé et nettoyé (espaces superflus supprimés)
    
    Examples:
        >>> valider_prenom("Jean")
        'Jean'
        >>> valider_prenom("  José  ")
        'José'
    """
    # Vérifier que le prénom n'est pas vide ou ne contient que des espaces
    if not prenom or not prenom.strip():
        # Afficher le message d'erreur sur stderr (sortie d'erreur standard)
        print("Erreur : Le prénom ne peut pas être vide", file=sys.stderr)
        # Quitter avec le code d'erreur 1
        sys.exit(1)
    
    # Retourner le prénom nettoyé (espaces superflus supprimés)
    return prenom.strip()


def echo_prenom(prenom):
    """
    Affiche un message de salutation avec le prénom fourni.
    
    Cette fonction affiche un message au format "Bonjour {prénom}!" dans
    la console standard (stdout). Elle respecte la casse et les caractères
    spéciaux du prénom fourni.
    
    Args:
        prenom (str): Le prénom à afficher (doit être non-vide et validé)
    
    Returns:
        None
    
    Examples:
        >>> echo_prenom("Jean")
        Bonjour Jean!
        >>> echo_prenom("José")
        Bonjour José!
    """
    # Afficher le message de salutation
    print(f"Bonjour {prenom}!")


def main():
    """
    Fonction principale du script.
    
    Orchestration du programme :
    1. Parse les arguments de la ligne de commande
    2. Valide le prénom fourni
    3. Affiche le message de salutation
    
    Returns:
        None (exit code 0 en cas de succès, 1 en cas d'erreur)
    """
    # Créer le parseur d'arguments
    parser = argparse.ArgumentParser(
        prog='script.py',
        description='Script Echo Prénom - Affiche votre prénom en réponse',
        epilog='Exemple: python script.py Jean',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        add_help=True
    )
    
    # Ajouter l'argument positional "prenom"
    parser.add_argument(
        'prenom',
        metavar='<prénom>',
        help='Votre prénom à afficher'
    )
    
    # Parser les arguments fournis en ligne de commande
    args = parser.parse_args()
    
    # Valider le prénom (quitte avec exit code 1 si invalide)
    prenom_valide = valider_prenom(args.prenom)
    
    # Afficher le message de salutation avec le prénom validé
    echo_prenom(prenom_valide)


# Point d'entrée du script
if __name__ == '__main__':
    main()
