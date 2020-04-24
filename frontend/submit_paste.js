class PasteForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  
  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    fetch('/api/paste/create_paste', {
      method: 'POST',
      body: this.state.value
    }).then(function(response) {
      response.text().then(function(text) {
        console.log(text);
      });
    });
    event.preventDefault();
  }
  
  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <input type="submit" value="Submit paste" />
        <br />
        <label>
          <textarea value={this.state.value} onChange={this.handleChange} />
        </label>
      </form>
    );
  }
  }