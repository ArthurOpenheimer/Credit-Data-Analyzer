from database import load_data
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay, make_scorer, recall_score
import matplotlib.pyplot as plt


def carregar_dados():
    df = load_data()
    return df


def separar_features_target(df):
    x = df.drop(columns=['kredit'])  # tudo menos kredit
    y = df['kredit']                 # target é kredit
    return x, y


def mostrar_distribuicao_classes(y):
    """
    mostra a distribuição das classes da variável kredit
    """
    print("Distribuição da variável target (kredit):")
    print(y.value_counts())
    print("Distribuição percentual:")
    print(y.value_counts(normalize=True))


def dividir_dados(x, y, test_size=0.2, random_state=42):
    """
    divisão dos dados de treino e teste (80% treino e 20% teste)
    """
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=test_size, random_state=random_state
    )
    return x_train, x_test, y_train, y_test


def recall_classe_ruim(y_true, y_pred):
    """
    calcular o recall da classe ruim para otimização do GridSearch, para buscar os melhores parâmetros para a decision tree
    """    
    return recall_score(y_true, y_pred, pos_label=0)


def buscar_melhores_parametros(x_train, y_train):
    """
    busca dos melhores hiperparâmetros para a decision tree, focando no recall da classe ruim (classe 0)
    """
    param_grid = {
        'max_depth': [3, 4, 5, 6, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 5, 10],
        'criterion': ['gini', 'entropy']
    }

    grid_search = GridSearchCV(
        DecisionTreeClassifier(random_state=42),
        param_grid,
        cv=5,
        scoring=make_scorer(recall_classe_ruim),
        n_jobs=-1
    )

    grid_search.fit(x_train, y_train)

    print("\nMelhores parâmetros encontrados:")
    print(grid_search.best_params_)

    print("\nMelhor score médio de validação cruzada (recall classe 0):")
    print(f"{grid_search.best_score_:.4f}")

    return grid_search.best_estimator_


def avaliar_modelo(modelo, x_test, y_test):
    """
    avaliação dos modelo nos dados de teste
    """
    y_pred = modelo.predict(x_test)

    print("\nAcurácia nos dados de teste:")
    print(f"{accuracy_score(y_test, y_pred):.4f}")

    print("\nMatriz de confusão:")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

    print("\nRelatório de classificação:")
    print(classification_report(y_test, y_pred))

    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=modelo.classes_)
    disp.plot(cmap='Blues')
    plt.show()


def main():
    df = carregar_dados()

    x, y = separar_features_target(df)

    mostrar_distribuicao_classes(y)

    x_train, x_test, y_train, y_test = dividir_dados(x, y)

    melhor_modelo = buscar_melhores_parametros(x_train, y_train)

    avaliar_modelo(melhor_modelo, x_test, y_test)


if __name__ == "__main__":
    main()
