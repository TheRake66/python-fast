import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import styles from './{{lower_item_name}}.module.scss';

export default function {{capitalize_item_name}}() {
  const { t } = useTranslation('', { keyPrefix: 'components.{{lower_item_name}}' });
  
  return (
    <div className={styles.container}>
      Bonjour le composant {{capitalize_item_name}} !
    </div>
  );
}