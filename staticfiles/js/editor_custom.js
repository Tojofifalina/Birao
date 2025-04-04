
function insertCardBootstrap() {
    const cardTemplate = `
<div class="card" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">Titre de la carte</h5>
    <p class="card-text">Voici un exemple de carte Bootstrap. Modifiez ce contenu.</p>
    <a href="#" class="btn btn-primary">Bouton</a>
  </div>
</div>
`;
    insertMarkdown(cardTemplate);
}

function insertTableBootstrap() {
    const tableTemplate = `
<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Colonne 1</th>
      <th scope="col">Colonne 2</th>
      <th scope="col">Colonne 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Donnée 1</td>
      <td>Donnée 2</td>
      <td>Donnée 3</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Donnée 4</td>
      <td>Donnée 5</td>
      <td>Donnée 6</td>
    </tr>
  </tbody>
</table>
`;
    insertMarkdown(tableTemplate);
}

function insertAlertBootstrap() {
    const alertTemplate = `
<div class="alert alert-warning" role="alert">
  Ceci est un exemple d'alerte Bootstrap.
</div>
`;
    insertMarkdown(alertTemplate);
}

// Fonction utilitaire pour insérer du texte Markdown
function insertMarkdown(markdownText) {
    const editor = window.markdownEditor; // Assurez-vous que l'éditeur est global
    if (editor) {
        const cursor = editor.getCursor();
        editor.replaceRange(markdownText, cursor);
    } else {
        alert("Impossible d'insérer : éditeur introuvable !");
    }
}
