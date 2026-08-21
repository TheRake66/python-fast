import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { useNavigate, useParams } from "react-router-dom";
import styles from './{{lower_name}}.module.scss';

interface {{capitalize_name}}Props {
  
}

export default function {{capitalize_name}}({}: {{capitalize_name}}Props) {
  const { t, i18n } = useTranslation('', { keyPrefix: 'components.{{lower_name}}' });
  const navigate = useNavigate();
  const { } = useParams();

  const [value, setValue] = useState('');

  const mount = () => {
    
  };
  
  const unmount = () => {
    
  };

  useEffect(() => {
    mount();
    return unmount;
  });
  
  return (
    <div className={styles.container}>
      Bonjour le composant {{capitalize_name}} !
    </div>
  );
}