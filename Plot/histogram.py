def hatch_histo(df: pd.DataFrame, t_age: int, M: int) -> None:
  plt.figure(figsize=(8,5))
  bins_full = range(int(rep_date_.max()//1)+1)
  n_full, bins_full, patches_full = plt.hist(df[df > 0], 
                                             bins=bins_full,
                                             histtype="step", color="b")
  bins_pred = range(t_age, t_age + M + 1)
  n_pred, bins_pred, patches_pred = plt.hist(df[(df >= t_age) & (df < t_age + M)],
                                             bins=bins_pred,
                                             histtype="step", color="r", fill=True)
  bins_after = range(t_age, int(df.max()//1)+1)
  n_after, bins_after, patches_after = plt.hist(df[df >= t_age],
                                                bins=bins_after,
                                                histtype="step", color="g", hatch="/")
  plt.xticks([0, 14, 20, 40, 60])
  plt.xlabel("battery age [month] at replacement")
  plt.ylabel("#batteries")
  plt.show()
