'use strict';

class Card extends React.Component {
  
  static get BACK_DEFAULT() {
    return 'back_red';
  }

  constructor(props) {
    super(props);
  }

  static to_url(card_name){
    const base_url = "/static/images/cards/";
    const img_ext = ".jpg";
    const card_url = base_url + card_name + img_ext;
    return card_url;
  }

  render() {

    return (
      <img className="card" src={Card.to_url(this.props.card_name)}/>
    );
  }
}