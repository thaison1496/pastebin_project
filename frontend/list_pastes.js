class ListPastes extends React.Component {
  constructor(props) {
    super(props);
    this.state = {pastes: []};
  }

  fetchPastes() {
    var tmp = this;
    fetch('/api/paste/list', {
      method: 'GET'
    }).then(function(response) {
      response.text().then(function(text) {
        tmp.setState({pastes: JSON.parse(text)});
      });
    });
  }

  componentDidMount() {
    this.fetchPastes();
  }
  
  renderPastes() {
    return this.state.pastes.map((paste) => 
      <tr>
        <td>
          <a href={"api/paste/" + paste[0]}>{paste[0]}</a>
        </td>
        <td>{paste[1]}</td>
        <td>{paste[2]}</td>
      </tr>);
  }

  render() {
    return (
      <table class="table table-sm table-hover">
        <thead>
          <tr>
            <th scope="col">paste_id</th>
            <th scope="col">content</th>
            <th scope="col">create_date</th>
          </tr>
        </thead>
        <tbody>
          {this.renderPastes()}
        </tbody>
      </table>
    );
  }
  }