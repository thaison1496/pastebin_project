const rootElement = document.getElementById('root')

// Create a function to wrap up your components
function App() {
  return (
    <div>
      <ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
        <li class="nav-item">
          <a class="nav-link active" id="pills-new-paste-tab" data-toggle="pill" href="#pills-new-paste" role="tab" aria-controls="pills-new-paste" aria-selected="true">
            New paste
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" id="pills-list-pastes-tab" data-toggle="pill" href="#pills-list-pastes" role="tab" aria-controls="pills-list-pastes" aria-selected="false">
            List pastes
          </a>
        </li>
      </ul> 
      <div class="tab-content" id="pills-tabContent">
        <div class="tab-pane fade show active" id="pills-new-paste" role="tabpanel" aria-labelledby="pills-new-paste-tab">
          <PasteForm />
        </div>
        <div class="tab-pane fade" id="pills-list-pastes" role="tabpanel" aria-labelledby="pills-list-pastes-tab">
          <ListPastes />
        </div>
      </div>
    </div>
  )
}

// Use the ReactDOM.render to show your component on the browser
ReactDOM.render(
  <App />,
  rootElement
)
