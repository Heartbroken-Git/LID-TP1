import LID_sequence_matcher as LseqMatch
import LID_event_retrieval as LeventRet
import LID_tests as Ltests

def main():

    # Étape 1 : Récupérer le flux

    # Étape 2 : Parser le flux à la recherche d'une requête ciblant nos trusted sites

    # Étape 3 : Réaliser les autres tests

    # Étape 4 : Noter l'URL

    # Étape 5 : Écrire sur un fichier les URL dites malveillantes

    # ===== TESTS =====
    LeventRet.connectFireHose('single_domain')

if __name__ == '__main__':
    main()
